function filter(value){
	
  	var sslctable = document.getElementById("ssdata");
	var semistable = document.getElementById("sedata");
	var school;

	for(var i=1;i<semistable.rows.length;i++){
		school=semistable.rows[i].innerHTML.replace(/<[^>]+>/g,"|").split("|")[3];
		res=school.toLowerCase().match(value.toLowerCase());
		if(res==value.toLowerCase()){
			semistable.rows[i].style.display='';
		}
		else{
			semistable.rows[i].style.display='none';
		}
	}
}

function clicks(value,type){
	if(type==1){
		var table=document.getElementById('ssdata');
		for(var i=0;i<=table.rows.length-1;i++){
			table.rows[i].bgColor='#FFFFFF';
		}	
	} else {
		table=document.getElementById('sedata');
		for(var i=0;i<=table.rows.length-1;i++){
			table.rows[i].bgColor='#FFFFFF';
		}
	}				
	if(value.bgColor=='#FFD700'){
	 	value.bgColor='#FFFFFF';
		if(type==1){
			var sslc=document.getElementById('sslc');
			sslc.value='';
		
		}
		else{
			var semis=document.getElementById('semis');
			semis.value='';
		
		}			
	}
	else
	{
	 	value.bgColor='#FFD700';
		if(type==1){
			var sslc=document.getElementById('sslc');
			sslc.value=value.innerHTML.replace(/<[^>]+>/g,"|").split("|")[1]+"|"+value.innerHTML.replace(/<[^>]+>/g,"|").split("|")[3]+"|"+value.innerHTML.replace(/<[^>]+>/g,"|").split("|")[5];
	
		}
		else{
			var semis=document.getElementById('semis');
			semis.value=value.innerHTML.replace(/<[^>]+>/g,"|").split("|")[1]+"|"+value.innerHTML.replace(/<[^>]+>/g,"|").split("|")[3]+"|"+value.innerHTML.replace(/<[^>]+>/g,"|").split("|")[5];

		}
	}
}

function myfunction()
{
	var x;
	var r=confirm("Sure you want to continue..??");
	if (r==true)
  	{
		document.forms["form1"].submit();
 	 }
	else
  	{
  		alert('You pressed Cancel!');
  	}
}

