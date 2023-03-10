function setCookie(cname,cvalue,exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires=" + d.toUTCString();
  let cookieVal = cname + "=" + cvalue + ";" + expires + ";path=/;";
  document.cookie = cookieVal;
}
  
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function darkthemeInit() {
  let darkthemeSwitch = document.querySelector('.darktheme-switch-container button.darktheme');

  if(getCookie("darktheme") == 'true') {
    darkthemeSwitch.classList.add('active');
    document.body.classList.add('darktheme');
  }

  darkthemeSwitch.addEventListener('click', (event) => {
    event.preventDefault();
    event.target.classList.toggle('active');
    document.body.classList.toggle('darktheme');
		
    if(document.body.classList.contains('darktheme')) {
      setCookie('darktheme', 'true', 365);
    }
    else {
      setCookie('darktheme', 'false', 365);
    }
  });
}