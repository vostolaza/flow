function connector(){
    var TokenAcceso = "MTU5MzAzMDMyMTE5OTo1Mzg3YWI1MGM3NWZkZGRlZGZkZjcyMGY5NGQ3Zg=="
    var data = document.getElementById('data').value
    var datosPOST= `evidence=aaaaaaaaaaaaaaaaaaaaa&data=` + data
    var request = new XMLHttpRequest();
    request.open("POST", "https://cors-anywhere.herokuapp.com/https://api.stamping.io/stamp/?"+datosPOST);
    request.setRequestHeader("Authorization", "Basic " + TokenAcceso);
    request.onreadystatechange = function () {
        if (this.readyState === 4) {
            console.log(this.responseText)
        resp = JSON.parse(this.responseText)
        console.log(resp)
        }
    }
    request.send()
}

// function sendAPI() {
//     hashvalue = document.getElementById('data').value;
//     var token = "MTU5MzAzMDMyMTE5OTo1Mzg3YWI1MGM3NWZkZGRlZGZkZjcyMGY5NGQ3Zg=="

//     stData = JSON.parse(hashvalue)
//     trxId = hex_sha1(stData.evidence);
//     var request = new XMLHttpRequest();
//     var str=""
//     if (typeof stData.evidence!=="undefined") str=str+'evidence='+stData.evidence
//     if (typeof stData.hash2!=="undefined") str=str+'&hash2='+stData.hash2
//     if (typeof stData.hash3!=="undefined") str=str+'&hash3='+stData.hash3
//     if (typeof stData.subject!=="undefined") str=str+'&subject='+stData.subject
//     if (typeof stData.data!=="undefined") str=str+'&data='+stData.data
//     if (typeof stData.url!=="undefined") str=str+'&url='+stData.url
//     if (typeof stData.reference!=="undefined") str=str+'&reference='+stData.reference
//     if (typeof stData.lat!=="undefined") str=str+'&lat='+stData.lat
//     if (typeof stData.long!=="undefined") str=str+'&long='+stData.long
//     if (typeof stData.transactionType!=="undefined") str=str+'&transactionType='+stData.transactionType

//     console.log('https://api.stamping.io/stamp/?'+str+"&token="+atob(token.replace("Authorization: Basic ","")).substr(14))
//     request.open('POST', 'https://api.stamping.io/stamp/?'+str+"&token="+atob(token.replace("Authorization: Basic ","")).substr(14));
//     console.log (atob(token.replace("Authorization: Basic ","")).substr(14));

//     request.onreadystatechange = function () {
//         if (this.readyState === 4) {
//             var myObj = JSON.parse(this.responseText);
//             console.log(this.responseText)
//             msgOk("Transaccion registrada", "TrxId: "+trxId+"", "Ok", "")
//         }

//     }
//     request.send()
// }