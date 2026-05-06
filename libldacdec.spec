%define _disable_source_fetch 1

Name:     libldacdec
Version:  1.0
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  APACHE+Proprietary
URL:      https://github.com/anonymix007/libldacdec
#Source0: https://github.com/EliasTheBigMasterofBullshit/libldacdec # Fork with hack to build libldacBT 
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

%build
git clone https://github.com/EliasTheBigMasterofBullshit/libldacdec
cd libldacdec
git submodule update --init --checkout
make libldacdec.so
patchelf --set-soname libldacBT_dec.so libldacdec.so
mv libldacdec.so libldacBT_dec.so


%install
install -m 777 -d "%{_buildroot}/libldacdec/libldacBT_dec.so" "%{_libdir}/libldacBT_dec.so"
install -m 644 -d "%{_sourcedir}/ldacBT-dec.pc" "%{_libdir}/pkgconfig/ldacBT-dec.pc"
install -m 644 -d "%{_buildroot}/libldacdec/libldacBT_dec.h" "%{_includedir}/libldacBT_dec.h"

%files
%{_libdir}/libldacBT_dec.so

%files devel
%{_libdir}/pkgconfig/ldacBT-dec.pc
%{_includedir}/libldacBT_dec.h

%changelog
