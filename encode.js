function encode(str){
    temp = str.charAt(0)
    count = 0
    newstr = ""
    for(var i = 0; i < str.length; i++){
      if(str.charAt(i)===temp)
        count++;
      else{
        if(count<3){
          for(var j = 0; j < count; j++)
            newstr += temp;
        }
        else{
          newstr += temp;
          newstr += count;
        }
        count = 1;
        temp = str.charAt(i);
      }
    }
    return newstr;
}
