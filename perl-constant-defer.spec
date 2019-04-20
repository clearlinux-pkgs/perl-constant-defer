#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-constant-defer
Version  : 6
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/constant-defer-6.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KR/KRYDE/constant-defer-6.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libc/libconstant-defer-perl/libconstant-defer-perl_6-1.debian.tar.xz
Summary  : 'Constant subs with deferred value calculation.'
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-constant-defer-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This file is part of constant-defer.
constant-defer is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 3, or (at
your option) any later version.

%package dev
Summary: dev components for the perl-constant-defer package.
Group: Development
Provides: perl-constant-defer-devel = %{version}-%{release}

%description dev
dev components for the perl-constant-defer package.


%package license
Summary: license components for the perl-constant-defer package.
Group: Default

%description license
license components for the perl-constant-defer package.


%prep
%setup -q -n constant-defer-6
cd ..
%setup -q -T -D -n constant-defer-6 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/constant-defer-6/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-constant-defer
cp COPYING %{buildroot}/usr/share/package-licenses/perl-constant-defer/COPYING
cp debian/copyright %{buildroot}/usr/share/package-licenses/perl-constant-defer/debian_copyright
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-constant-defer/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/constant/defer.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/constant::defer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-constant-defer/COPYING
/usr/share/package-licenses/perl-constant-defer/debian_copyright
/usr/share/package-licenses/perl-constant-defer/deblicense_copyright
