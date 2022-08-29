$('#recButton').addClass("notRec");

function Click(){
	if($('#recButton').hasClass('notRec')){
		$('#recButton').removeClass("notRec");
		$('#recButton').addClass("Rec");
	}
	else{
		$('#recButton').removeClass("Rec");
		$('#recButton').addClass("notRec");
	}
};