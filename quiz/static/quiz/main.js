//countdown timer
var endtime = endTimeOfTest.getTime();
// Run myfunc every second
var myfunc = setInterval(function () {
  var starttime = new Date().getTime();
  var timeleft = endtime - starttime;

  // Calculating the days, hours, minutes and seconds left
  var days = Math.floor(timeleft / (1000 * 60 * 60 * 24));
  var hours = Math.floor((timeleft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((timeleft % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((timeleft % (1000 * 60)) / 1000);

  // console.log("End time:");
  // console.log(days, hours, minutes, seconds);

  // Result is output to the specific element
  if (days <= 0) {
    document.getElementById("days").innerHTML = "";
  } else {
    document.getElementById("days").innerHTML = days + "d ";
  }

  if (hours <= 0) {
    document.getElementById("hours").innerHTML = "";
  } else {
    document.getElementById("hours").innerHTML = hours + "h ";
  }

  if (minutes <= 0) {
    document.getElementById("mins").innerHTML = "";
  } else {
    document.getElementById("mins").innerHTML = minutes + "m ";
  }

  if (seconds <= 0) {
    document.getElementById("secs").innerHTML = "";
  } else {
    document.getElementById("secs").innerHTML = seconds + "s ";
  }

  // Display the message when test is over
  if (timeleft < 0) {
    clearInterval(myfunc);
    alert("Test has been ended");
  }
}, 1000);
