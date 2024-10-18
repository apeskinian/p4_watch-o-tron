var inc = 1000;

clock();

function clock() {
  const date = new Date();

  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();
  
  const hour = hours * 30;
  const minute = minutes * 6;

  const accurateHour = hour + minutes * 0.5;
  const accurateMinute = minute + seconds * 0.1;
  
  document.querySelector('.hour').style.transform = `rotate(${accurateHour}deg)`
  document.querySelector('.minute').style.transform = `rotate(${accurateMinute}deg)`
}

setInterval(clock, inc);
