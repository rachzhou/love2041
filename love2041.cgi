#!/usr/bin/perl -w
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
require 'love2041.cgi';

my $q = new CGI;

print $q->header;

print $q->start_html(-title => 'Login page');


print "Please sign in\n";
print "Username: ";
$user = <STDIN>;

print "Password: "
$password = <STDIN>;

if (defined $user) {
    open F, "<$student/profile.txt" or die "can not open $student/profile.txt: $!";

    if (defined $password) { #if a password is entered
        $correct = getPassword($username);


        chomp $correct;
        if($password eq $correct) {
            print ("You have logged in!");
        } else {
            print ("The password you have entered is incorrect");
        }
    } else {
        print ("Please enter a password");
    }
}

    #look for username in archives and then check if password matches whats there
    #if username doesnt match then print error message
    #if un matches but pw doesnt, print error message





