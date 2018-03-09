var Bob = function(){};


Bob.prototype.hey = function(statement){
	statement = statement.trim();
	str = statement;
	if (statement.length == 0 || !str.replace(/\s/g, '').length){
		return "Fine. Be that way!";
	}
	var regex1 = /[a-zA-Z]/
	var is_question = (statement.substr(statement.length-1)=="?");
	if (regex1.test(statement)){
		var is_yelling =  (statement == statement.toUpperCase());
	}
	if (is_question && is_yelling){
		return "Calm down, I know what I'm doing!";
	} else if (is_question && !is_yelling){
		return "Sure.";
	} else if (!is_question && is_yelling){
		return "Whoa, chill out!";
	} else {
		return "Whatever."
	}
}

module.exports = Bob;
