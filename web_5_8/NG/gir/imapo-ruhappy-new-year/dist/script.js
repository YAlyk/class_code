function garland() {
  nums = document.getElementById('nums_1').innerHTML
  if (nums == 1) {
    document.getElementById('garland').className = 'garland_1';
    document.getElementById('nums_1').innerHTML = '2'
  }
  if (nums == 2) {
    document.getElementById('garland').className = 'garland_2';
    document.getElementById('nums_1').innerHTML = '3'
  }
  if (nums == 3) {
    document.getElementById('garland').className = 'garland_3';
    document.getElementById('nums_1').innerHTML = '4'
  }
  if (nums == 4) {
    document.getElementById('garland').className = 'garland_4';
    document.getElementById('nums_1').innerHTML = '1'
  }
}

setInterval(function() {
  garland()
}, 600)