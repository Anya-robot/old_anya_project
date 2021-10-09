var handled = false;
window.addEventListener("keydown", function (event) {
  if (event.defaultPrevented) {
    return; // Should do nothing if the default action has been cancelled
  }
  var handled2 = false;
  if ((event.key !== undefined) && (handled == false)) {
    if (event.keyCode == 87) {
      window.open("/action1" , "_top");
	  handled = true;
	  handled2 = true;
    }
	else if (event.keyCode == 65) {
      window.open("/action2" , "_top");
	  handled = true;
	  handled2 = true;
    }
	else if (event.keyCode == 83) {
      window.open("/action3" , "_top");
	  handled = true;
	  handled2 = true;
    }
	else if (event.keyCode == 68) {
      window.open("/action2" , "_top");
	  handled = true;
	  handled2 = true;
    } 
  else if (event.keyCode !== undefined) {
    
	
    // Handle the event with KeyboardEvent.keyCode and set handled true.
  }
  }

  if (handled2) {
    // Suppress "double action" if event handled
    event.preventDefault();
  }
}, true);
window.addEventListener("keyup", function (event) {
  if (event.defaultPrevented) {
    return; // Should do nothing if the default action has been cancelled
  }
  var handled2 = false;
  if (event.key !== undefined) {
    if (event.keyCode == 87) {
	  handled = false;
	  handled2 = true;
    }
	else if (event.keyCode == 65) {
	  handled = false;
	  handled2 = true;
    }
	else if (event.keyCode == 83) {
	  handled = false;
	  handled2 = true;
    }
	else if (event.keyCode == 68) {
      window.open("/action2" , "_top");
	  handled = false;
	  handled2 = true;
    } 
  }
  else if (event.keyCode !== undefined) {
    
	
    // Handle the event with KeyboardEvent.keyCode and set handled true.
  }

  if (handled2) {
    // Suppress "double action" if event handled
    event.preventDefault();
  }
}, true);