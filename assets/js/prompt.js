// Ensure the window is loaded properly
window.addEventListener('load', () => {
  // Get the send button
  const sendButton = document.getElementById('sendButton');
  // Add an event listener to the button
  sendButton.addEventListener('click', sendMessage);
});


function openAi(api_key, model, prompt, temperature, max_tokens) {
  return new Promise((resolve, reject) => {
      const req = new XMLHttpRequest();
      req.onreadystatechange = function () {
          if (this.readyState == 4) {
              resolve(JSON.parse(this.responseText));
          } else {
              reject('Unable to complete openAI request');
          }
      };

      req.open('POST', 'https://api.openai.com/v1/completions');
      req.setRequestHeader('Content-Type', 'application/json');
      req.setRequestHeader('Authorization', 'Bearer ' + api_key);

      req.send(JSON.stringify({
          "model": model,
          "prompt": prompt,
          "temperature": temperature,
          "max_tokens": max_tokens
      })); 

  }); 
} 




function queryAPI(authorization, org) {

  var url = "https://api.openai.com/v1/engines/text-davinci-003/completions";
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
  
 // queryAPI("Bearer YOUR_API_KEY", "");


 async function sendMessage() {

  console.log("sendMessage called");
  // Get input text
  var inputText = document.getElementById("inputfield").value;
  // Call the API and get response
  //let response = await openAi("", "text-davinci-003", "Say this is a test", 0, 20);
  let response = "";

  const Http = new XMLHttpRequest();
  const url='https://jsonplaceholder.typicode.com/posts';
  Http.open("GET", url);
  Http.send();
  
  Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
  }


  console.log(response);
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