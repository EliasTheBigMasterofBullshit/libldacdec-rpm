%define _disable_source_fetch 1

Name:     libldacdec
Version:  1.0
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  APACHE+Proprietary
URL:      https://github.com/anonymix007/libldacdec
#Source1: https://android.googlesource.com/platform/external/libldac.git #commit=e8ff0f96f26b84b47711c549e0d60baa425cd70e
Source2: ldacBT-dec.pc

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
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

%build
cd %{_sourcedir}
git clone https://github.com/anonymix007/libldacdec
cd libldacdec
git submodule update --init --checkout
make libldacdec.so
patchelf --set-soname libldacBT_dec.so libldacdec.so
mv libldacdec.so libldacBT_dec.so


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
mkdir -p  $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
install -m 777 -d "%{_sourcedir}/libldacdec/libldacBT_dec.so" "%{_buildroot}/%{_libdir}/libldacBT_dec.so"
install -m 644 -d "%{_source0}/ldacBT-dec.pc" "%{_buildroot}/%{_libdir}/pkgconfig/ldacBT-dec.pc"
install -m 644 -d "%{_sourcedir}libldacdec/libldacBT_dec.h" "%{_buildroot}/%{_includedir}/libldacBT_dec.h"

%files
%{_libdir}/libldacBT_dec.so

%files devel
%{_libdir}/pkgconfig/ldacBT-dec.pc
%{_includedir}/libldacBT_dec.h

%changelog
