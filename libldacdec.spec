%define _disable_source_fetch 1

Name:     libldacdec
Version:  1.0
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  Proprietary
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


%build
git clone https://github.com/EliasTheBigMasterofBullshit/libldacdec
cd libldacdec
git submodule update --init --checkout
make libldacdec.so


%install
%make_install 


%files

%changelog
