%define _disable_source_fetch 0

Name:     libldacdec
Version:  1.0
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  APACHE+Proprietary
URL:      https://github.com/anonymix007/libldacdec
Source0: https://github.com/EliasTheBigMasterofBullshit/libldacdec/releases/download/workflow_10/libldacdec-1.0.tar.gz
Source1: ldacBT-dec.pc


BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel

Requires: libsndfile
Requires: libsamplerate

%description
Reverse-engineered unofficial LDAC Bluetooth decoder library

%package devel
Requires: libldacdec
Summary: libldacdec development files
Provides: libldacdec-devel

%description devel
Reverse-engineered unofficial LDAC Bluetooth decoder library, development files

%prep	
%autosetup -n  libldacdec -p1

%build
$PREFIX=/usr/lib64 make ldacdec

%install
%make_install
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_libdir}/pkg-config/ldacBT-dec.pc

%files
%{_libdir}/libldacBT_dec.so

%files devel
%{_libdir}/pkg-config/ldacBT-dec.pc
%{_includedir}/libldacBT_dec.h

