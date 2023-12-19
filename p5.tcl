pg5.tcl

set ns [new Simulator -multicast on]
set tf [open ex5.tr w]
$ns trace-all $tf
set nf [open ex5.nam w]
$ns namtrace-all $nf

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]

$ns duplex-link $n0 $n2 0.5Mb 10ms DropTail
$ns duplex-link $n1 $n2 0.5Mb 10ms DropTail
$ns duplex-link $n3 $n2 0.5Mb 10ms DropTail
$ns duplex-link $n3 $n4 0.5Mb 10ms DropTail
$ns duplex-link $n4 $n6 0.5Mb 10ms DropTail
$ns duplex-link $n4 $n5 0.5Mb 10ms DropTail
$ns duplex-link $n3 $n7 0.5Mb 10ms DropTail

$n0 label "Source1"
$n1 label "Source2"
$n5 label "Receiver1"
$n6 label "Receiver2"
$n7 label "Receiver3"

#packet coloring
$ns color 1 blue
$ns color 2 red
#node coloring
$n5 color blue
$n6 color blue
$n7 color blue

set udp1 [new Agent/UDP]
$ns attach-agent $n0 $udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1

set udp2 [new Agent/UDP]
$ns attach-agent $n1 $udp2
set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $udp2

$udp1 set fid_ 1
$udp2 set fid_ 2

set mproto DM
set mrthandle [$ns mrtproto $mproto {}]

set grp1 [Node allocaddr]
set grp2 [Node allocaddr]

$udp1 set dst_addr_ $grp1
$udp1 set dst_port_ 0
$udp2 set dst_addr_ $grp2
$udp2 set dst_port_ 0

set null1 [new Agent/Null]
$ns attach-agent $n5 $null1
set null2 [new Agent/Null]
$ns attach-agent $n6 $null2
set null3 [new Agent/Null]
$ns attach-agent $n7 $null3
set null4 [new Agent/Null]
$ns attach-agent $n5 $null4
set null5 [new Agent/Null]
$ns attach-agent $n6 $null5
set null6 [new Agent/Null]
$ns attach-agent $n7 $null6

$ns at 0.5 "$cbr1 start"
$ns at 9.5 "$cbr1 stop"
$ns at 0.5 "$cbr2 start"
$ns at 9.5 "$cbr2 stop"

$ns at 1.0 "$n5 join-group $null1 $grp1"
$ns at 1.5 "$n6 join-group $null2 $grp1"
$ns at 2.0 "$n7 join-group $null3 $grp1"
$ns at 2.5 "$n5 join-group $null4 $grp2"
$ns at 3.0 "$n6 join-group $null5 $grp2"
$ns at 3.5 "$n7 join-group $null6 $grp2"

$ns at 4.0 "$n5 leave-group $null1 $grp1"
$ns at 4.5 "$n6 leave-group $null2 $grp1"
$ns at 5.0 "$n7 leave-group $null3 $grp1"
$ns at 5.5 "$n5 leave-group $null4 $grp2"
$ns at 6.0 "$n6 leave-group $null5 $grp2"
$ns at 6.5 "$n7 leave-group $null6 $grp2"

$ns at 10.0 "finish"

proc finish {} {
global tf nf ns
$ns flush-trace
close $tf
close $nf
puts "running nam..."
exec nam ex5.nam &
exit 0
}

$ns run
