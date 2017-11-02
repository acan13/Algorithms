function flatten(arr){
  for(var i = 0; i < arr.length; i++){
    if(Array.isArray(arr[i])){
      arr.slice(0,i-1).concat(flatten(arr[i])).concat(arr.slice(i+1,arr.length));
    }
  }
  return arr
}
