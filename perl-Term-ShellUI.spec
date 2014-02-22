%define upstream_name    Term-ShellUI
%define upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Parse a string into tokens
License:    MIT
Group:      Development/Perl
Url:        https://github.com/bronson/Term-ShellUI
Source0:    http://search.cpan.org/CPAN/authors/id/B/BR/BRONSON/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel
BuildArch: noarch

%description
Term::ShellUI uses the history and autocompletion features of the
Term::ReadLine manpage to present a sophisticated command-line interface to
the user. It tries to make every feature that one would expect to see in a
fully interactive shell trivial to implement. You simply declare your
command set and let ShellUI take care of the heavy lifting.

This module was previously called the Term::GDBUI manpage.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

