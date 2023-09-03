<?php

#question 11
class Person{

}
class Employee extends Person{
    public $position,$salary;
    function __construct($pos, $sal){
        $this->position=$pos;
        $this->salary=$sal;
    }
    function display_details(){
        echo "Position ".$this->position." has ".$this->salary." salary";
    }
}

#question 12
interface Comparable{
    public function compare();
}
class Product implements Comparable{
    public $name,$price;

    public function __construct($nm,$pri){
        $this->name=$nm;
        $this->price=$pri;
    }
    public function compare($obj){
        echo $this->price>$obj->price;
    }
}

#question 13
class Logger{
    public static $logcount=0;
    public static function log($message) {
        echo $message . "</br>";
        self::$logcount++;
    }
}

#question 14
class Math{
    public static function add($a,$b){
        return $a+$b;
    }
    public static function sub($a,$b){
        return $a-$b;
    }
    public static function mult($a,$b){
        return $a*$b;
    }
}

#question 15
class File{
    public $name,$size;
    public function __construct($nm,$sz){
        $this->name=$nm;
        $this->size=$sz;
    }
    public function total_size($arr){
        $total = 0;

        foreach ($arr as $file) {
            if ($file instanceof File) {
                $total += $file->size;
            }
        }
    }
}

#question 16
class Calculator {
    private $result;
    function __construct() {
        $this->result = 0;
    }
    function get_result() {
        return $this->result;
    }
    function add($num) {
        $this->result += $num;
    }
    function subtract($num) {
        $this->result -= $num;
    }
}

#question 17
class ShCart {
    private $items,$total;
    function __construct() {
        $this->items = [];
        $this->total = 0;
    }
    public function add_item($items, $price) {
        $this->items[$items] = $price;
        $this->total += $price;
    }
    public function get_total() {
        return $this->total;
    }
}

#question 18

#question 19
class Validation {
    public static function validate_email($email) {
        return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
    }
    public static function validate_password($pass) {
        return strlen($pass) >= 8;
    }
    public static function validate_field($fi) {
        return !empty($fi);
    }
}

?>

