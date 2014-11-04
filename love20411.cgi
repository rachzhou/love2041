#!/usr/bin/perl -w

# written by andrewt@cse.unsw.edu.au September 2013
# as a starting point for COMP2041/9041 assignment 2
# http://cgi.cse.unsw.edu.au/~cs2041/assignments/LOVE2041/

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use Data::Dumper;  
use List::Util qw/min max/;
warningsToBrowser(1);

#require login.pl;

use CGI::Cookie;

%cookies = fetch CGI::Cookie;
$usern = "Rachael";
$usern = $cookies{'id'}->value if $cookies{'id'};
#$username++;

print header(-cookie=>"id=$usern"); 
print start_html("-title"=>"LOVE2041", -style=>{-src=>['//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css']});
%cookies = CGI::Cookie->fetch;
print "un: ", $cookies{'id'}->value, "<br>";

#



#hashes for information of the people
my @students = glob("./students/*"); #array of student usernames

my %birthdate;
my %courses;
my %degree;
my %email;
my %favourite_bands;
my %favourite_books;
my %favourite_hobbies;
my %favourite_movies;
my %favourite_TV_shows;
my %gender;
my %hair_colour;
my %height;
my %name;
my %password;
my %username;
my %weight;

for $student (@students) {
    open F, "<$student/profile.txt" or die "can not open $student/profile.txt: $!";
    #print "$student\n";
    my $username = $student;
    $username =~ s/\.\/students\///;

    #hashing the students information
    LINE: while ($line = <F>) {
        if ($line =~ m/"^birthdate:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $date = chomp($line);
                $birthdate{$username} = $date;
            }
        }
        if ($line =~ m/"^courses:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $course = chomp($line);
                push(@{$courses{$username}}, $course); #adding each course into the array
            }
        }
        if ($line =~ m/"^degree:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $deg = chomp($line);
                $degree{$username} = $deg;
            }
        }
        if ($line =~ m/"^email:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $mail = chomp($line);
                $email{$username} = $mail;
            }
        }
        if ($line =~ m/"^favourite_bands:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $bands = chomp($line);
                push(@{$favourite_bands{$username}}, $bands); #adding each course into the array
            }
        }
        if ($line =~ m/"^favourite_books:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $books = chomp($line);
                push(@{$favourite_books{$username}}, $books); #adding each course into the array
            }
        }
        if ($line =~ m/"^favourite_hobbies:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $hobbies = chomp($line);
                push(@{$favourite_hobbies{$username}}, $hobbies); #adding each course into the array
            }
        }
        if ($line =~ m/"^favourite_movies:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $movies = chomp($line);
                push(@{$favourite_movies{$username}}, $movies); #adding each course into the array
            }
        }
        if ($line =~ m/"^favourite_TV_shows:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $shows = chomp($line);
                push(@{$favourite_TV_shows{$username}}, $shows); #adding each course into the array
            }
        }
        if ($line =~ m/"^gender:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $gen = chomp($line);
                $gender{$username} = $gen;
            }
        }
        if ($line =~ m/"^email:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $mail = chomp($line);
                $email{$username} = $mail;
            }
        }
        if ($line =~ m/"^hair_colour:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $colour = chomp($line);
                $hair_colour{$username} = $colour;
            }
        }
        if ($line =~ m/"^height:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $cm = chomp($line);
                $height{$username} = $cm;
            }
        }
        if ($line =~ m/"^name:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $nam = chomp($line);
                $name{$username} = $nam;
            }
        }
        if ($line =~ m/"^password:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $pw = chomp($line);
                $password{$username} = $pw;
            }
        }
        if ($line =~ m/"^weight:$"/) {
            while ($line = <F>) {
                if($line =~ m/"^.*\:$"/){
                    redo LINE;
                }

                my $kg = chomp($line);
                $weight{$username} = $kg;
            }
        }
    }
}



#sub getPassword($username){
#    if (exists $password{$username}){
#        return $password{$username};            
#    } else {
#        return undef;
#    }
#}

# some globals used through the script
$debug = 1;
$students_dir = "./students";

print browse_screen();
print page_trailer();
exit 0; 

sub browse_screen {
    my $n = param('n') || 0;
    my @students = glob("$students_dir/*");
    $n = min(max($n, 0), $#students);
    param('n', $n + 1);
    my $student_to_show  = $students[$n];
    my $profile_filename = "$student_to_show/profile.txt";
    open my $p, "$profile_filename" or die "can not open $profile_filename: $!";

    #hides rid of personal information
    while ($line1 = <$p>){
        if($skipLines == 0){
            if($line1 =~ /^(name:|password:|email:|courses:)$/){
                $skipLines = 1;
            }else{
                $profile .= $line1;
            }
        }else{
            if(not($line1 =~ /^(name:|password:|email:|courses:)$/)){
                if($line1 =~ /:$/){
                $profile .= $line;
                $skipLines = 0;
                }
            }
        }
    }

    #print website name and profile pic
    print center(h2(b("Matchalicious Definitious")));
    print img({ src => "$student_to_show/profile.jpg"}), "\n\n";
    #$profile = join '', <$p>;

    close $p;
    
    return p,
        start_form, "\n",
        pre($profile),"\n",
        hidden('n', $n + 1),"\n",
        submit('Next student'),"\n",
        end_form, "\n",
        p, "\n";
}


#
# HTML placed at bottom of every screen
# It includes all supplied parameter values as a HTML comment
# if global variable $debug is set
#
sub page_trailer {
    my $html = "";
    $html .= join("", map("<!-- $_=".param($_)." -->\n", param())) if $debug;
    $html .= end_html;
    return $html;
}
