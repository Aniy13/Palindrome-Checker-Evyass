function clearPage() {
    console.log("Clear button clicked");
    // Reset the form fields
    document.getElementById("palindromeForm").reset(); 
    
    
    document.getElementById("entered-word").value = "";
    document.getElementById("reversed-word").value = "";
    document.getElementById("result").value = "";
}
