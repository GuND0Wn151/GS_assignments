<?php

#1 question
setcookie("Username","Gulnara Serik",time()+3600);

#2 question
echo "<br>".$_COOKIE["Username"];

#3 question
setcookie("Username","",time()-3600);

#4 question
session_start();
$_SESSION["userid"]=10020;

#5 question
echo "<br>The session variable for userid is ".$_SESSION["userid"];

#6 question
$_SESSION=[];
session_destroy();

#7 question
#secure cookie can be set by doing a 6th parameter as true, which can be sent throught encrypted connection
setcookie("username","ram",time()-3600,"/","",true);

#8 question
setcookie("visited","yes");
if(isset($_COOKIE["visited"])){
    echo "<br>This cookie is set ".$_COOKIE["visited"];
}else{
    echo "Cookie is not set";
}

#9 question
session_start();
if(isset($_SESSION["preferences"])){
    $_SESSION["preferences"]=array("name"=>"Ram","id"=>"2020","sal"=>"20000");
}

#10 question
if(isset($_SESSION["preferences"])){
    $data = $_SESSION["preferences"];
    foreach ($data as $key => $value) {
        echo $key . ": " . $value . "</br>";
    }
}

#11 question
$timeout = 1800;
$lasttime = $_SESSION["LAST_ACTIVITY"];
$currenttime = time();
$differencetime = $currenttime - $lasttime;

if($differencetime>$timeout){
    session_unset();
    session_destroy();
    echo "Session is dead";
}else{
    echo "Session still active";
}


#14
session_regenerate_id(true);


#16 question
setcookie("NewCookie", "myvalue1", time() + 3600, "/");
$_SESSION["NewCookie"] = "different value_session";


?>


