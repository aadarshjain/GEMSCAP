<?php

$servername = "localhost";
$username = "root";
$password = "";
$db = "GEMSCAP";

$conn = mysqli_connect($servername, $username, $password, $db);
if(mysqli_connect_error()){
	die();
}

if(isset($_POST['aadarsh'])){

	$Employ_id= $_POST['employ_id'];
	$First_name = $_POST['fname'];
	$Middle_name = $_POST['mname'];
	$Last_name = $_POST['lname'];
	$Father_name = $_POST['father_name'];
	$Mother_name = $_POST['mother_name'];
	$P_address = $_POST['p_address'];
	$L_address = $_POST['l_address'];
	$Email_Id = $_POST['email_Id'];
	$Contact_number1 = $_POST['contact_number1'];
	$Contact_number2 = $_POST['contact_number2'];
	$DOB = $_POST['dob'];
	$Gender = $_POST['gender'];
	$Marital = $_POST['marital'];
	$Aadhar_Card = $_POST['aadhar_card'];
	$Pan_Card = $_POST['pan_card'];
	$Family_Persons_Name_1= $_POST['family_Persons_Name_1'];
	$Family_Persons_Contact_Number_1 = $_POST['family_Persons_Contact_Number_1'];
	$Family_Persons_Relation_With_Employee1= $_POST['family_Persons_Relation'];
	$Family_Persons_Name_2= $_POST['family_Persons_Name_2'];
	$Family_Persons_Contact_Number_2= $_POST['family_Persons_Contact_Number_2'];
	$Family_Persons_Relation_With_Employee2= $_POST['family_Persons_Relation'];
	$Educational_Course_Name = $_POST['educational_Course_Name'];
	$Passing_Year = $_POST['passing_Year'];
	$Passing_Status = $_POST['passing_Status'];
	$PF_Nominee_name = $_POST['pf_nominee_name'];
	$PF_Nominee_relation = $_POST['pf_nominee_relation'];
	$PF_Nominee_DOB= $_POST['pf_nominee_DOB'];
	$Date_Of_Joining = $_POST['doj'];
	$Date_Of_Resigning = $_POST['dor'];
    $Account_Number_1=$_POST['acc_no_1'];
    $Ifsc_Code_1=$_POST['ifsc_code_1'];
    $Bank_Name_1=$_POST['bank_name_1'];
    $Account_Type_1=$_POST['acc_type_1'];
    $Account_Holder_Name_1=$_POST['acc_holder_name_1'];
    $Account_Number_2=$_POST['acc_no_2'];
    $Ifsc_Code_2=$_POST['ifsc_code_2'];
    $Bank_Name_2=$_POST['bank_name_2'];
    $Account_Type_2=$_POST['acc_type_2'];
    $Account_Holder_Name_2=$_POST['acc_holder_name_2'];

	$sql = "INSERT INTO gemscap_user (Employ_id,First_name,Middle_name,Last_name,Father_name, Mother_name, P_address, L_address, Email_Id, Contact_number1, Contact_number2, DOB, Gender, Marital, Aadhar_Card, Pan_Card, Family_Persons_Name_1, Family_Persons_Contact_Number_1, Family_Persons_Relation_With_Employee1,Family_Persons_Name_2, Family_Persons_Contact_Number_2, Family_Persons_Relation_With_Employee2, Educational_Course_Name,Passing_Year, Passing_Status,PF_Nominee_name,PF_Nominee_relation,PF_Nominee_DOB,Date_Of_Joining,Date_Of_Resigning,Account_Number_1,Ifsc_Code_1,Bank_Name_1,Account_Type_1,Account_Holder_Name_1,Account_Number_2,Ifsc_Code_2,Bank_Name_2,Account_Type_2,Account_Holder_Name_2) VALUES ('".$Employ_id."','".$First_name."','".$Middle_name."','".$Last_name."','".$Father_name."','".$Mother_name."','".$P_address."','".$L_address."','".$Email_Id."','".$Contact_number1."','".$Contact_number2."','".$DOB."','".$Gender."','".$Marital."','".$Aadhar_Card."','".$Pan_Card."','".$Family_Persons_Name_1."','".$Family_Persons_Contact_Number_1."','".$Family_Persons_Relation_With_Employee1."','".$Family_Persons_Name_2."','".$Family_Persons_Relation_With_Employee2."','".$Family_Persons_Contact_Number_2."','".$Educational_Course_Name."','".$Passing_Year."','".$Passing_Status."','".$PF_Nominee_name."','".$PF_Nominee_relation."','".$PF_Nominee_DOB."','".$Date_Of_Joining."','".$Date_Of_Resigning."','".$Account_Number_1."','".$Ifsc_Code_1."','".$Bank_Name_1."','".$Account_Type_1."','".$Account_Holder_Name_1."','".$Account_Number_2."','".$Ifsc_Code_2."','".$Bank_Name_2."','".$Account_Type_2."','".$Account_Holder_Name_2."')";

	if(mysqli_query($conn,$sql)) {

		echo "success";

	} else {

		echo mysqli_error($conn);

	}
		
}
?>


<!DOCTYPE html>
<html lang = "en">
<head>
  <meta charset = "UTF-8">
  <title>USER PROFILE</title>
  
  <link rel = "stylesheet" href = "user_profile.css">
</head>
<body>
  <div class = "profile">
    <h1 class = "label">EMPLOYEE'S PERSONAL INFORMATION</h1>
    <form class = "User_profile" autocomplete = "off" method = "post" name = "form" onsubmit = "return validated()">
      <a href = "home.html" class = "previous">&laquo; Back</a>
      <div class = "font">Employee ID</div>
      <input type = "text" name = "employ_id" required>
      <div id = "error">Please fill up details</div>
      <div class = "font">First Name</div>
      <input type = "text" name = "fname" required>
      <div id = "error">Please fill up name</div>
      <div class = "font">Middle Name</div>
      <input type = "text" name = "mname" required>
      <div id = "error">Please fill up Middle Name</div>
      <div class = "font">Last Name</div>
      <input type = "text" name = "lname" required>
      <div id = "error">Please fill up Last Name</div>
      <div class = "font">Father's Name</div>
      <input type = "text" name = "father_name" required>
      <div id = "error">Please fill up Name</div>
      <div class = "font">Mother's Name</div>
      <input type = "text" name = "mother_name" required>
      <div id = "error">Please fill up Name</div>
      <div class = "font">Date Of Birth</div>
      <input type = "date" name = "dob" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Gender</div>
      <input type="radio" id="male" name="gender" value="male">
      <label for="male">Male</label><br>
      <input type="radio" id="female" name="gender" value="female">
      <label for="female">Female</label><br>
      <input type="radio" id="other" name="gender" value="other">
      <label for="other">Other</label><br>
      <div class = "font">Marital Status</div>
      <input type="radio" id="Married" name="marital" value="Married">
      <label for="Married">Married</label><br>
      <input type="radio" id="Unmarried" name="marital" value="Unmarried">
      <label for="Unmarried">Unmarried</label><br>
      <input type="radio" id="other" name="marital" value="other">
      <label for="other">Other</label><br>
      <h2>EMPLOYEE'S CONTACT INFORMATION</h2>
      <div class = "font">Permanent Address</div>
      <input type = "text" name = "p_address" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Local Address</div>
      <input type = "text" name = "l_address" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Email Address</div>
      <input type="email" name = "email_Id" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Contact Number 1</div>
      <input type = "tel" name = "contact_number1"  required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Contact Number 2</div>
      <input type = "tel" name = "contact_number2" >
      <div id = "error">Please fill up required field</div>
      <div class = "font">Family Person's Name 1</div>
      <input type = "text" name = "family_Persons_Name_1" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Family Person's Contact Number</div>
      <input type = "text" name = "family_Persons_Contact_Number_1" pattern = "^(\+91){1}[1-9]{1}[0-9]{9}$"  required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Family Persons Relation With Employee:</div>
      <input type = "text" name = "family_Persons_Relation" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Family Person's Name 2</div>
      <input type = "text" name = "family_Persons_Name_2" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Family Person's Contact Number</div>
      <input type = "text" name = "family_Persons_Contact_Number_2" pattern = "^(\+91){1}[1-9]{1}[0-9]{9}$"	 required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Family Persons Relation With Employee</div>
      <input type = "text" name = "family_Persons_Relation" required>
      <div id = "error">Please fill up required field</div>
      <h2>EMPLOYEE'S DOCUMENTS INFORMATION</h2>
      <div class = "font">Aadhar Card</div>
      <input type = "text" name = "aadhar_card" pattern = "^([0-9]){12}$" required>
      <!input type="file" id="myFile" name="filename">
      <div id = "error">Please fill up required field</div>
      <div class = "font">PAN Card</div>
      <input type = "text" name = "pan_card" pattern = "^[A-Z]{5}[0-9]{4}[A-Z]{1}$" required>
      <!input type="file" id="myFile" name="filename">
      <div id = "error">Please fill up required field</div>
      <h2>EMPLOYEE'S EDUCATIONAL DETAILS</h2>
      <div class = "font">Educational Course Name</div>
      <input type = "text" name = "educational_Course_Name" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Passing Year</div>
      <input type = "month" name = "passing_Year" required>
      <div id = "error">Please fill up required field</div>
      <div class = "font">Employee's Passing Status</div>
      <input type="radio" id="passed With Distinction" name="passing_Status" value="Passed With Distinction">
      <label for="male">Passed With Distinction</label><br>
      <input type="radio" id="Failed" name="passing_Status" value="Failed">
      <label for="female">Failed</label><br>
      <input type="radio" id="other" name="passing_Status" value="other">
      <label for="other">Other</label><br>
      <div class = "font">PF Nominee name</div>
      <input type = "text" name = "pf_nominee_name" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">PF Nominee relation</div>
      <input type = "text" name = "pf_nominee_relation" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">PF Nominee DOB</div>
      <input type = "date" name = "pf_nominee_DOB" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Date Of Joining</div>
      <input type = "date" name = "doj" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Date Of Resigning</div>
      <input type = "date" name = "dor" >
      <div id = "error">Please fill up required details</div>
      <h2>EMPLOYEE'S BANK ACCOUNT DETAILS</h2>
      <div class = "font">Account Number 1</div>
      <input type = "text" name = "acc_no_1" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">IFSC Code </div>
      <input type = "text" name = "ifsc_code_1" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Bank Name</div>
      <input type = "text" name = "bank_name_1" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Account Type</div>
      <input type = "text" name = "acc_type_1" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Account Holder Name</div>
      <input type = "text" name = "acc_holder_name_1" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Account Number 2</div>
      <input type = "text" name = "acc_no_2" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">IFSC Code </div>
      <input type = "text" name = "ifsc_code_2" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Bank Name</div>
      <input type = "text" name = "bank_name_2" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Account Type</div>
      <input type = "text" name = "acc_type_2" required>
      <div id = "error">Please fill up required details</div>
      <div class = "font">Account Holder Name</div>
      <input type = "text" name = "acc_holder_name_2" required>
      <div id = "error">Please fill up required details</div>
      <button type = "submit" name="aadarsh" formaction = "after_user.html" value = "send">Submit</button>
      <button type = "button" onClick = "window.print()">Print</button>
      <!button type = "reset"><!/button>
    </form>
  </div>
  <script src = "user_profile.js"></script>
</body>
</html>