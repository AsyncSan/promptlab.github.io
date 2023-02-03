// Ensure the window is loaded properly
window.addEventListener('load', () => {
  // Get the send button
  const sendButton = document.getElementById('sendButton');
  // Add an event listener to the button
  sendButton.addEventListener('click', sendMessage);
});



function queryAPI(url, authorization, org) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        // Process response
        console.log(this.responseText);
      }
    };
    xhr.open("GET", url, true);
    xhr.setRequestHeader("Authorization", authorization);
    xhr.setRequestHeader("OpenAI-Organization", org);
    xhr.send();
  }
  
 // queryAPI("https://api.openai.com/v1/models", "Bearer YOUR_API_KEY", "org-reyhJK05Ya3s4pyJG4zMBe7r");


 function sendMessage() {
  console.log("sendMessage called");
  // Get input text
  var inputText = document.getElementById("inputfield").value;
  // Call the API and get response
  var response = callAPI(inputText);
  // Display the response
  displayMessage(response);
}

function callAPI(inputText) {
  console.log("sendMessage called");
  console.log(inputText);
  // API call code here
  var response = inputText;
  return response;
}

function displayMessage(message) {
  console.log("displayMessage called");
  console.log(message);
  // Get the display field
  var displayField = document.getElementById("displayfield");
  // Append the message to the display field
  displayField.value += message + "\n";
  // Scroll to the bottom of the display field
  displayField.scrollTop = displayField.scrollHeight;
}