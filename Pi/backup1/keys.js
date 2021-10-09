window.addEventListener("keyup", function (event) {
  if (event.defaultPrevented) {
    return; // Should do nothing if the default action has been cancelled
  }

  var handled = false;
  if (event.key !== undefined) {

    if (event.keyCode == 87) {
      window.open("/movestop" , "_top");
 handled = true;
    }
else if (event.keyCode == 65) {
      window.open("/movestop" , "_top");
 handled = true;
    }
else if (event.keyCode == 83) {
      window.open("/moverstop" , "_top");
 handled = true;
    }
else if (event.keyCode == 68) {
      window.open("/movestop" , "_top");
 handled = true;
    }
  }
  else if (event.keyCode !== undefined) {
   

    // Handle the event with KeyboardEvent.keyCode and set handled true.
  }

  if (handled) {
    // Suppress "double action" if event handled
    event.preventDefault();
  }
}, true);


window.addEventListener("keydown", function (event) {
  if (event.defaultPrevented) {
    return; // Should do nothing if the default action has been cancelled
  }

  var handled = false;
  if (event.key !== undefined) {
    if (event.keyCode == 87) {
      window.open("/movefstart" , "_top");
	  handled = true;
    }
	else if (event.keyCode == 65) {
      window.open("/movelstart" , "_top");
 handled = true;
    }
else if (event.keyCode == 83) {
      window.open("/moverstart" , "_top");
 handled = true;
    }
else if (event.keyCode == 68) {
      window.open("/movebstart" , "_top");
 handled = true;
    }
  }
  else if (event.keyCode !== undefined) {
   

    // Handle the event with KeyboardEvent.keyCode and set handled true.
  }

  if (handled) {
    // Suppress "double action" if event handled
    event.preventDefault();
  }
}, true);
