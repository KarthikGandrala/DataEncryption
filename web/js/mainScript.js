
// Following statement is used to toggle display of each function

showContent("homePage");

// Following function allows for dispay of each item in the menu

function showContent(clickLinkId) {

    // Get the current active menu id and clear it

    if (document.getElementById("activeMenu").value != undefined) {

        // Set the current menu value to null

        currentMenu = document.getElementById("activeMenu").value;

        // Display the current menu to the user

        document.getElementById(currentMenu).style.display = "none";
    }

    // When a different link has been clicked, block the current menu item

    document.getElementById(clickLinkId).style.display = "block";
    document.getElementById("activeMenu").value = clickLinkId;
}

// This function is is written to clear all menu boxes

function clearBox(e1, e2)
{

    // Sets all the values in the boxes to null/nothing

    document.getElementById(e1).innerHTML = "";
    document.getElementById(e2).innerHTML = "";
}

function stopSpace(event) {
    var k = event ? event.which : window.event.keyCode;
    if (k == 32) return false;
}

function postBasicRotate() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/basicEncrypt");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange even
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result1").innerHTML = this.responseText;
        }
    };

    // buid javascript object
     var data = {
                    data: document.getElementById("bsrm").value,
                    key: document.getElementById("bsrk").value
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function postBasicRotate2() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/basicDecrypt");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result2").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("bsrmd").value,
                    key: document.getElementById("bsrkd").value
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function postPoly1() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/polyEncrypt");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result3").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("pm").value,
                    key: document.getElementById("pe").value
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function postPoly2() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/polyDecrypt");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result4").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("pmd").value,
                    key: document.getElementById("ped").value
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function postXor1() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/xorEncrypt");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result5").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("xm").value,
                    key: document.getElementById("xk").value
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function postXor2() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/xorDecrypt");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result6").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("xmd").value,
                    key: document.getElementById("xkd").value
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function custom1() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object
    request.open("POST", "/cE");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result7").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("CE").value,
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}

function custom2() {
    // creating the XMLHttpRequest object
    var request = new XMLHttpRequest();
  
    // Instantiating the request object`
    request.open("POST", "/cD");
    request.setRequestHeader("Content-Type", "application/json");
    // This line is to define the event listener for readystatexchange event
    request.onreadystatechange = function () {
        // checks is request is sucess
        if (this.readyState === 4 && this.status === 200) {

            // Inserting response from server
            
            document.getElementById("result8").innerHTML = this.responseText;
        }
    };
    // buid javascript object
     var data = {
                    data: document.getElementById("CD").value,
                }
    // Request is sent to the server
    // convert javascript object to string before sending it to the API
    request.send(JSON.stringify(data));
}