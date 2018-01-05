function partition(arr){
  if (arr.length === 1)
    return 0

  var pivot_point = Math.floor(Math.random()*arr.length)
  var pivot = arr.splice([pivot_point],1)[0]
  for(var i = 0, pos = 0; i !== arr.length; i++){
    if(arr[pos] >= pivot)
      arr.push(arr.splice(pos,1)[0])
    else
      pos++
  }
  arr.splice(pos,0,pivot)
  return pos
}

function quick_sort(arr){
  if(arr.length === 0)
    return []
  if(arr.length < 2){
    partition(arr)
    return arr
  }
  else{
    var pivot = partition(arr)
    return quick_sort(arr.splice(0,pivot)).concat(quick_sort(arr))
  }
}

console.log(quick_sort([2,6,1,8,4,5,3,9,7]))
