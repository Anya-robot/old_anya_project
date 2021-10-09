window.addEventListener("keyup", function (event) {
  if (event.defaultPrevented) {
    return; // Should do nothing if the default action has been cancelled
  }

  var handled = false;
  if (event.key !== undefined) {

    if (event.keyCode == 68) {
      window.open("/action1" , "_top");
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
      window.open("/action1" , "_top");
	  handled = true;
    }
	else if (event.keyCode == 65) {
      window.open("/action2" , "_top");
	  handled = true;
    }
	else if (event.keyCode == 83) {
      window.open("/action3" , "_top");
	  handled = true;
    }
	else if (event.keyCode == 68) {
      window.open("/action2" , "_top");
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





  