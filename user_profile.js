var fname = document.forms['form']['fname']
var mname = document.forms['form']['mname']
var lname = document.forms['form']['lname']
var father_name = document.forms['form']['father_name']
var mother_name = document.forms['form']['mother_name']
var p_address = document.forms['form']['p_address']
var l_address = document.forms['form']['l_address']
var email_Id = document.forms['form']['email_Id']
var contact_number1 = document.forms['form']['contact_number1']
var contact_number2 = document.forms['form']['contact_number2']
var dob = document.forms['form']['dob']
var gender = document.forms['form']['gender']
var marital = document.forms['form']['marital']
var aadhar_card = document.forms['form']['aadhar_card']
var pan_card = document.forms['form']['pan_card']
var family_Persons_Name = document.forms['form']['family_Persons_Name']
var family_Persons_Contact_Number = document.forms['form']['family_Persons_Contact_Number']
var family_Persons_Relation = document.forms['form']['family_Persons_Relation']
var educational_Course_Name = document.forms['form']['educational_Course_Name']
var passing_Year = document.forms['form']['passing_Year']
var passing_Status = document.forms['form']['passing_Status']

var error = document.getElementById('error')

fname.addEventListener('textInput', fname_Verify);
mname.addEventListener('textInput', mname_Verify);
lname.addEventListener('textInput', lname_Verify);
father_name.addEventListener('textInput', father_name_Verify);
mother_name.addEventListener('textInput', mother_name_Verify);
p_address.addEventListener('textInput', p_address_Verify);
l_address.addEventListener('textInput', l_address_Verify);
email_Id.addEventListener('textInput', email_Id_Verify);
contact_number1.addEventListener('textInput', contact_number1_Verify);
contact_number2.addEventListener('textInput', contact_number2_Verify);
dob.addEventListener('textInput', dob_Verify);
gender.addEventListener('textInput', gender_Verify);
marital.addEventListener('textInput', marital_Verify);
aadhar_card.addEventListener('textInput', aadhar_card_Verify);
pan_card.addEventListener('textInput', pan_card_Verify);
family_Persons_Name.addEventListener('textInput', family_Persons_Name_Verify);
family_Persons_Contact_Number.addEventListener('textInput', family_Persons_Contact_Number_Verify);
family_Persons_Relation.addEventListener('textInput', family_Persons_Relation_Verify);
educational_Course_Name.addEventListener('textInput', educational_Course_Name_Verify);
passing_Year.addEventListener('textInput', passing_Year_Verify);
passing_Status.addEventListener('textInput', passing_Status_Verify);

function validated(){
	if (fname.value < 0) {
		fname.style.border = "1px solid red";
		error.style.display = "block";
		fname.focus();
		return false;
	}
	if (mname.value < 0) {
		mname.style.border = "1px solid red";
		error.style.display = "block";
		mname.focus();
		return false;
	}	
	if (lname.value < 0) {
		lname.style.border = "1px solid red";
		error.style.display = "block";
		lname.focus();
		return false;
	}
	if (father_name.value < 0) {
		father_name.style.border = "1px solid red";
		error.style.display = "block";
		father_name.focus();
		return false;
	}
	if (mother_name.value < 0) {
		mother_name.style.border = "1px solid red";
		error.style.display = "block";
		mother_name.focus();
		return false;
	}
	if (p_address.value < 0) {
		p_address.style.border = "1px solid red";
		error.style.display = "block";
		p_address.focus();
		return false;
	}	
	if (l_address.value < 0) {
		l_address.style.border = "1px solid red";
		error.style.display = "block";
		l_address.focus();
		return false;
	}
	if (email_Id.value < 0) {
		email_Id.style.border = "1px solid red";
		error.style.display = "block";
		email_Id.focus();
		return false;
	}
	if (contact_number1.value < 0) {
		contact_number1.style.border = "1px solid red";
		error.style.display = "block";
		contact_number1.focus();
		return false;
	}
	if (contact_number2.value < 0) {
		contact_number2.style.border = "1px solid red";
		error.style.display = "block";
		contact_number2.focus();
		return false;
	}
	if (dob.value < 0) {
		dob.style.border = "1px solid red";
		error.style.display = "block";
		dob.focus();
		return false;
	}
	if (gender.value < 0) {
		gender.style.border = "1px solid red";
		error.style.display = "block";
		gender.focus();
		return false;
	}
	if (marital.value < 0) {
		marital.style.border = "1px solid red";
		error.style.display = "block";
		marital.focus();
		return false;
	}
	if (aadhar_card.value < 0) {
		aadhar_card.style.border = "1px solid red";
		error.style.display = "block";
		aadhar_card.focus();
		return false;
	}
	if (pan_card.value < 0) {
		pan_card.style.border = "1px solid red";
		error.style.display = "block";
		pan_card.focus();
		return false;
	}
	if (family_Persons_Name.value < 0) {
		family_Persons_Name.style.border = "1px solid red";
		error.style.display = "block";
		family_Persons_Name.focus();
		return false;
	}
	if (family_Persons_Contact_Number.value < 0) {
		family_Persons_Contact_Number.style.border = "1px solid red";
		error.style.display = "block";
		family_Persons_Contact_Number.focus();
		return false;
	}
	if (family_Persons_Relation.value < 0) {
		family_Persons_Relation.style.border = "1px solid red";
		error.style.display = "block";
		family_Persons_Relation.focus();
		return false;
	}
	if (educational_Course_Name.value < 0) {
		educational_Course_Name.style.border = "1px solid red";
		error.style.display = "block";
		educational_Course_Name.focus();
		return false;
	}
	if (passing_Year.value < 0) {
		passing_Year.style.border = "1px solid red";
		error.style.display = "block";
		passing_Year.focus();
		return false;
	}
	if (passing_Status.value < 0) {
		passing_Status.style.border = "1px solid red";
		error.style.display = "block";
		passing_Status.focus();
		return false;
	}
			
}
function fname_Verify() {
	if (fname.value.length >= 5) {
		fname.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
	}
}
function mname_Verify() {
	if (mname.value.length >= 5) {
		mname.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function lname_Verify() {
	if (lname.value.length >= 5) {
		lname.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function father_name_Verify() {
	if (father_name.value.length >= 5) {
		father_name.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function mother_name_Verify() {
	if (mother_name.value.length >= 5) {
		mother_name.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function p_address_Verify() {
	if (p_address.value.length >= 5) {
		p_address.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function l_address_Verify() {
	if (l_address.value.length >= 5) {
		l_address.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function email_Id_Verify() {
	if (email_Id.value.length >= 5) {
		email_Id.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function contact_number1_Verify() {
	if (contact_number1.value.length >= 5) {
		contact_number1.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function contact_number2_Verify() {
	if (contact_number2.value.length >= 5) {
		contact_number2.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function dob_Verify() {
	if (dob.value.length >= 5) {
		dob.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function gender_Verify() {
	if (gender.value.length >= 5) {
		gender.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function marital_Verify() {
	if (marital.value.length >= 5) {
		marital.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function aadhar_card_Verify() {
	if (aadhar_card.value.length >= 5) {
		aadhar_card.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function pan_card_Verify() {
	if (pan_card.value.length >= 5) {
		pan_card.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function family_Persons_Name_Verify() {
	if (family_Persons_Name.value.length >= 5) {
		family_Persons_Name.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function family_Persons_Contact_Number_Verify() {
	if (family_Persons_Contact_Number.value.length >= 5) {
		family_Persons_Contact_Number.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function family_Persons_Relation_Verify() {
	if (family_Persons_Relation.value.length >= 5) {
		family_Persons_Relation.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function educational_Course_Name_Verify() {
	if (educational_Course_Name.value.length >= 5) {
		educational_Course_Name.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function passing_Year_Verify() {
	if (passing_Year.value.length >= 5) {
		passing_Year.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}
function passing_Status_Verify() {
	if (passing_Status.value.length >= 5) {
		passing_Status.style.border = "1px solid silver";
		error.style.display = "none";
		return true;	
    }
}