//<script src="assets\js\p5.js"></script>
function setup() {
      // check if the device is running on mobile
  isMobile = (navigator.userAgent.indexOf("Mobile") !== -1);

  if (isMobile) {
    var canvas = createCanvas(windowWidth, windowHeight);

    canvas.parent('container');
  }
  }
  
  function draw() {
    if (isMobile) {
      if (mouseIsPressed) {
        fill(0);
      } else {
        fill(255);
      }
      ellipse(mouseX, mouseY, 80, 80);
    }

  }