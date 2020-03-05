Goal: Advance a user when they click a certain answer choice.

Code (to be put in Qualtrics addOnload JS):

var qobj = this;  
	jQuery("#Buttons").hide();
	jQuery("#"+this.questionId+" [choiceid=1]").click(function() { qobj.clickNextButton(); });
  
 Notes:
 - Note the space before [choiceid=1].
 - You can see/change the choiceid's for a question by clicking the gear and going to "Recode Values"
 - By default, for example, for a multiple choice question, the first answer choice is 1, the second 2, ...
 - Can change the final "clickNextButton()" call to have something else happen when they click the answer choice
