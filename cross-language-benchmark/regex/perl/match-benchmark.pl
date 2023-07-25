#!/usr/bin/env perl

for (my $i = 100*1000*1000; --$i >= 0; ) {
	"some-string-for-match" =~ m/s\w+g/;
}
