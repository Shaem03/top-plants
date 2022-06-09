const base_url = 'http://0.0.0.0:5000'
export function getRegion() {
    const url = base_url + '/api/region'
    return fetch(url)
        .then(data => data.json())
}

export function filterByRegion(abbr, top_n) {
    let url = ""
    if (abbr != null) {
        url = base_url + '/api/filter?region=' + abbr + "&top=" + top_n
    } else {
        url = base_url + '/api/filter?&top=' + top_n
    }

    return fetch(url)
        .then(data => data.json())
}