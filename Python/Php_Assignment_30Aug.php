<?php
function calculate_debt($a) {
    $debt = 100000;
    for ($i = 0; $i < $a; $i++) {
        $interest = $debt * 0.05;
        $debt += $interest;
        $debt = ceil($debt / 1000) * 1000; 
    }
    return $debt;
}

function Circles($x1,$y1,$x2,$y2,$r1,$r2){

    $d=sqrt(($x1-$x2)*($x1-$x2)+($y1-$y2)*($y1-$y2));
    if($d<=$r1-$r2){
        echo "Circle C1 in C2";
    }elseif($d<=$r2-$r1){
        echo "Cicle C2 in C1";
    }elseif($d<$r1+$r2){
        echo "C1 and C2 intersect";
    }elseif($d==$r1+$r2){
        echo "C1 and C2 touch each other";
    }else{
        "C1 and C2 dont touch each other";
    }

}

function Orthogonal($x1,$y1,$x2,$y2,$x3,$y3,$x4,$y4){

    $slope1=($y2-$y1)/($x2-$x1);
    $slope2=($y4-$y3)/($x4-$x3);
    if($slope1*$slope2==-1){
        echo "They can form a orthogonal line";
    }else{
        echo "They are not orthogonal lines";
    }
}

$a = 10000;
$finalDebt = calculate_debt($a);
echo "Total debt  $a: $finalDebt";
?>