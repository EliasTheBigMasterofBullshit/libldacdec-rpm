Name:     libldacdec
Version:  1.0
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  Proprietary
URL:      https://github.com/anonymix007/libldacdec
Source0: https://github.com/anonymix007/libldacdec
Source1: https://android.googlesource.com/platform/external/libldac.git#commit=e8ff0f96f26b84b47711c549e0d60baa425cd70e
Source2: ldacBT-dec.pc

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: patchelf


%description
Reverse-engineered unofficial LDAC Bluetooth decoder library

%prep
git submodule init
git submodule set-url libldac "$srcdir/libldac"
git -c protocol.file.allow=always submodule update


%build
make ldacdec
patchelf --set-soname libldacBT_dec.so libldacdec.so
mv libldacdec.so libldacBT_dec.so

%install
install -Dm 0755 "%{SOURCE0}/libldacdec/libldacBT_dec.so" "$RPM_BUILD_ROOT/usr/lib/libldacBT_dec.so"
install -Dm 0644 "%{SOURCE0}/libldacdec/libldacBT_dec.h" "$RPM_BUILD_ROOT/usr/include/ldac/ldacBT_dec.h"
install -Dm 0644 "%{SOURCE2}/ldacBT-dec.pc" "$RPM_BUILD_ROOT/usr/lib/pkgconfig/ldacBT-dec.pc"


%files

%changelog
