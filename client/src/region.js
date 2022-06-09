export function getRegion() {
    const url = '/api/region'
    return fetch(url)
        .then(data => data.json())
}


export function filterByRegion(abbr, top_n) {
    let url = ""
    if (abbr != null) {
        url = '/api/filter?region=' + abbr + "&top=" + top_n
    } else {
        url = '/api/filter?&top=' + top_n
    }

    return fetch(url)
        .then(data => data.json())
}