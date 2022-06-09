export function getRegion() {
    const url = 'http://127.0.0.1:8081/api/region'
    return fetch(url)
        .then(data => data.json())
}

export function filterByRegion(abbr, top_n) {
    let url = ""
    if (abbr != null) {
        url = 'http://127.0.0.1:8081/api/filter?region=' + abbr + "&top=" + top_n
    } else {
        url = 'http://127.0.0.1:8081/api/filter?&top=' + top_n
    }

    return fetch(url)
        .then(data => data.json())
}