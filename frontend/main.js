window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount()
})

const functionApiUrl = 'https://getmyresumecounter.azurewebsites.net/api/GetResumeCounter?code=lgiQjdl4Vb55Yl0i35nhLnmalOy5Iu0nqxv1Gu1Ojp84OMnm7ulZvw=='
const localfunctionApi = 'http://localhost:7071/api/GetResumeCounter'

const getVisitCount = () => {
    let count = 30
    fetch(functionApiUrl).then(response => {
        return response.json()
    }).then(response => {
        console.log("Website called function API.")
        count = response.count
        document.getElementById("counter").innerText = count
    }).catch(function(error){
        console.log(error)
    })
    return count
}
