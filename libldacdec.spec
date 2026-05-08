%define _disable_source_fetch 0

Name:     libldacdec
Version:  1.0
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  APACHE+Proprietary
URL:      https://github.com/anonymix007/libldacdec
Source0: https://github.com/EliasTheBigMasterofBullshit/libldacdec/releases/download/workflow_18/libldacdec-1.0.tar.gz
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
export PREFIX=%{_libdir}
make libldacBT_dec.so 

%install
export PREFIX=%{_libdir}
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libldacBT_dec.so.1
ln -sf $RPM_BUILD_ROOT/%{_libdir}/libldacBT_dec.so $RPM_BUILD_ROOT/%{_libdir}/libldacBT_dec.so.1
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_libdir}/pkg-config/ldacBT-dec.pc

%files
%{_libdir}/libldacBT_dec.so

%files devel
%{_libdir}/pkg-config/ldacBT-dec.pc
%{_includedir}/libldacBT_dec.h

