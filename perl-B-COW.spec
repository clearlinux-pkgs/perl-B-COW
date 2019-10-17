#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-COW
Version  : 0.001
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/B-COW-0.001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/B-COW-0.001.tar.gz
Summary  : 'B::COW additional B helpers to check COW status'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-B-COW-data = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution B-COW,
version 0.001:
B::COW additional B helpers to check COW status

%package data
Summary: data components for the perl-B-COW package.
Group: Data

%description data
data components for the perl-B-COW package.


%package dev
Summary: dev components for the perl-B-COW package.
Group: Development
Requires: perl-B-COW-data = %{version}-%{release}
Provides: perl-B-COW-devel = %{version}-%{release}
Requires: perl-B-COW = %{version}-%{release}

%description dev
dev components for the perl-B-COW package.


%prep
%setup -q -n B-COW-0.001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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

%files data
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/B/COW.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/B/COW/COW.so

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::COW.3
