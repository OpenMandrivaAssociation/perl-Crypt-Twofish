%define modname	Crypt-Twofish
%define modver	2.14

Summary:	Crypt-Twofish module for perl 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
Twofish is a 128-bit symmetric block cipher with a variable length (128, 192,
or 256-bit) key, developed by Counterpane Labs. It is unpatented and free for
all uses, as described at http://www.counterpane.com/twofish.html.

This module implements Twofish encryption. It supports the Crypt::CBC interface

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*/Crypt/Twofish.pm
%{perl_vendorlib}/*/auto/Crypt/Twofish
%{_mandir}/man3/*

