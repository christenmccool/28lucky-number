function snakeToCamel(str) {
    let strArray = str.split('_');

    let newString = strArray[0];

    strArray = strArray.slice(1);

    if (strArray.length > 0) {
 
        for (word of strArray) {
            newString += word[0].toUpperCase() + word.slice(1)
        }
    
    }
    
    return newString;
}
    


