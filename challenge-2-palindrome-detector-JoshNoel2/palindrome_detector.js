/*
* Adds isPalindrome function to the String prototype.
* Adding the function to the String prototype removes the need to receive the input as a parameter and run any typeof checks as a result of that.
* Takes ignorePunctuation as a parameter, defaults to false.
* Setting ignorePunctuation to true will only check the string's English letters and will ignore case.
*/
String.prototype.isPalindrome = function(ignorePunctuation=false) {
	//Get an array of the string's characters.
	//'this' represents the string that is being tested as the String type object.
	var s = this.valueOf().split("");
	while (true) {
		//If there are no more characters to check then return true.
		if (s.length < 1) {
			return true;
		}
		var i = 0; //First character of the array
		var j = s.length - (i+1); //Last character of the array
		if (ignorePunctuation) {
			//If the character is the same in upper case as it is lower case (not a letter), then remove it and continue.
			if (s[i].toLowerCase() == s[i].toUpperCase()) {
				s.splice(i, 1);
				continue;				
			}
			if (s[j].toLowerCase() == s[j].toUpperCase()) {
				s.splice(j, 1);
				continue;
			}
			//Set all characters to lowercase to ignore case.
			var a = s[i].toLowerCase();
			var b = s[j].toLowerCase();
		} else {
			//If ignorePunctuation is false then simply take the first and last characters without checking first.
			var a = s[i];
			var b = s[j];
		}
		if (a != b) { //If the first and last characters do not equal each other then return false.
			return false;
		}
		//Remove the first and last characters to do the next check with the second and second to last characters.
		s.splice(i, 1);
		s.splice(j-1, 1);
	}
}