#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-COW
Version  : 0.003
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/B-COW-0.003.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/B-COW-0.003.tar.gz
Summary  : 'B::COW additional B helpers to check COW status'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-B-COW-license = %{version}-%{release}
Requires: perl-B-COW-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution B-COW,
version 0.003:
B::COW additional B helpers to check COW status

%package dev
Summary: dev components for the perl-B-COW package.
Group: Development
Provides: perl-B-COW-devel = %{version}-%{release}
Requires: perl-B-COW = %{version}-%{release}

%description dev
dev components for the perl-B-COW package.


%package license
Summary: license components for the perl-B-COW package.
Group: Default

%description license
license components for the perl-B-COW package.


%package perl
Summary: perl components for the perl-B-COW package.
Group: Default
Requires: perl-B-COW = %{version}-%{release}

%description perl
perl components for the perl-B-COW package.


%prep
%setup -q -n B-COW-0.003
cd %{_builddir}/B-COW-0.003

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-COW
cp %{_builddir}/B-COW-0.003/LICENSE %{buildroot}/usr/share/package-licenses/perl-B-COW/dd4e29f997e82e723b165d30ec39001443a74f4d
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::COW.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-B-COW/dd4e29f997e82e723b165d30ec39001443a74f4d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/B/COW.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/B/COW/COW.so
