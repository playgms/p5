set ns [new Simulator -multicast on]
set tf [open p5.tr w]
$ns trace-all $tf
set nf [open p5.nam w]
$ns namtrace-all $nf
for {set i 0} {$i<8} {incr i} {
 set n$i [$ns node]
}
$ns duplex-link $n0 $n2 2Mb 2ms DropTail
$ns duplex-link $n1 $n2 2Mb 2ms DropTail
$ns duplex-link $n2 $n3 2Mb 2ms DropTail
$ns duplex-link $n3 $n4 2Mb 2ms DropTail
$ns duplex-link $n3 $n7 2Mb 2ms DropTail
$ns duplex-link $n4 $n5 2Mb 2ms DropTail
$ns duplex-link $n4 $n6 2Mb 2ms DropTail

set mproto DM
set mrthandle [$ns mrtproto $mproto {} ]
set group1 [Node allocaddr]
set group2 [Node allocaddr]

set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0
set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0

set udp1 [new Agent/UDP]
$ns attach-agent $n1 $udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1

$udp0 set dst_addr_ $group1
$udp0 set dst_port_ 0
$udp1 set dst_addr_ $group2
$udp1 set dst_port_ 0

set r1 [new Agent/Null]
$ns attach-agent $n2 $r1
set r2 [new Agent/Null]
$ns attach-agent $n3 $r2
set r3 [new Agent/Null]
$ns attach-agent $n4 $r3
set r4 [new Agent/Null]
$ns attach-agent $n5 $r4
set r5 [new Agent/Null]
$ns attach-agent $n6 $r5
set r6 [new Agent/Null]
$ns attach-agent $n7 $r6

$ns at 1.0 "$n2 join-group $r1 $group1"
$ns at 1.5 "$n3 join-group $r2 $group1"
$ns at 2.0 "$n4 join-group $r3 $group1"
$ns at 2.5 "$n5 join-group $r4 $group2"
$ns at 3.0 "$n6 join-group $r5 $group2"
$ns at 3.5 "$n7 join-group $r6 $group2"

$ns at 4.0 "$n2 leave-group $r1 $group1"
$ns at 4.5 "$n3 leave-group $r2 $group1"
$ns at 5.0 "$n4 leave-group $r3 $group1"
$ns at 5.5 "$n5 leave-group $r4 $group2"
$ns at 6.0 "$n6 leave-group $r5 $group2"
$ns at 6.5 "$n7 leave-group $r6 $group2"

$ns at 0.5 "$cbr0 start"
$ns at 0.5 "$cbr1 start"
$ns at 9.5 "$cbr0 stop"
$ns at 9.5 "$cbr1 stop"
$ns at 10.0 "finish"

$n0 label "source 1"
$n1 label "source 2"
$udp0 set fid_ 1
$udp1 set fid_ 2
$ns color 1 blue
$ns color 2 green

$n5 color blue 
$n6 color blue
$n7 color blue
$n5 label "reviever 1"
$n6 label "reciever 2"
$n7 label "reciever 3"

proc finish {} {
global ns tf nf
$ns flush-trace
close $tf
close $nf
exec nam p5.nam &
exit 0
}

$ns run





