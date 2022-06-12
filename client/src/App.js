import {useEffect, useState} from "react";
import Map from "./components/Map";
import Header from "./components/Header";
import {filterByRegion, getRegion} from "./region";

function App() {
    const [plantsData, setPlantsData] = useState([])
    const [regionData, setRegionData] = useState([])
    const [topN, setTopN] = useState([])
    const [selectedRegion, setSelectedRegion] = useState([])
    const [loading, setLoading] = useState(false)

    const handleTopSearch = (event) => {
        const value = event.target.value.toLowerCase();
        if (value >= 1) {
            setTopN(value.toString())
            filterByRegion(selectedRegion, value)
                .then(items => {
                    setPlantsData(items)
                })
        }
    }

    const filterRegion = (event) => {
        let value = event.target.value;
        if (value != null) {
            setSelectedRegion(value)
            filterByRegion(value, topN)
                .then(items => {
                    setPlantsData(items)
                })
        }
    }

    useEffect(() => {
        setLoading(true)
        filterByRegion(null, 10)
            .then(items => {
                setPlantsData(items)
            })

        getRegion()
            .then(reg => {
                setRegionData(reg)
            })

        setLoading(false)
    }, [])

    return (
        <div>
            <Header/>
            <center>
                Top n = <input type="text" placeholder="Search" onChange={(event) => handleTopSearch(event)}/>
                <select
                    className="form-control"
                    onChange={(event) => filterRegion(event)}
                >
                    <option key='1' value={null}>Select Region to Filter</option>
                    {regionData.map((item, index) => (
                        <option key={index} value={item.acronym}>
                            {item.name}
                        </option>
                    ))}
                </select>
            </center>
            {!loading ? <Map plantsData={plantsData}/> : <h1>Loading</h1>}
        </div>
    )
}

export default App;
