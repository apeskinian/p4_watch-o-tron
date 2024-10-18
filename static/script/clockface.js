var inc = 60000;

clock();

function clock() {
  const date = new Date();

  const hours = date.getHours();
  const minutes = date.getMinutes();
  
  const hour = hours * 30;
  const minute = minutes * 6;
  
  document.querySelector('.hour').style.transform = `rotate(${hour}deg)`
  document.querySelector('.minute').style.transform = `rotate(${minute}deg)`
}

setInterval(clock, inc);
