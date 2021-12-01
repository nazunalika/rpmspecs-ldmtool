%define srcname libldm
%define sover  1_0-0
%define major 0
%define minor 2
%define micro 5

Name:           ldmtool
Version:        %{major}.%{minor}.%{micro}
Release:        1%{?dist}
Summary:        A tool to manage Windows dynamic disks
License:        GPLv3
Group:          System/Base

URL:            https://github.com/mdbooth/libldm 
Source0:        https://github.com/mdbooth/%{srcname}/archive/refs/tags/%{srcname}-%{version}.tar.gz
#Patch0:         Remove-deprecated-g_type_class_add_private.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  json-glib-devel >= 0.14.0
BuildRequires:  libtool
BuildRequires:  pkgconfig(uuid)
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(zlib)

Requires:       %{srcname}-%{sover} = %{version}-%{release}

%description
Command-line tool for managing Microsoft Windows dynamic disks, which use
Microsoft's LDM metadata. It can inspect them, and also create and remove
device-mapper block devices which can be mounted.

%package -n %{srcname}-%{sover}
Summary:        Library to manage Windows dynamic disks
License:        LGPLv3
Group:          System/Libraries

%description -n %{srcname}-%{sover}
Library for managing Microsoft Windows dynamic disks, which use Microsoft's
LDM metadata. It can inspect them, and also create and remove device-mapper
block devices which can be mounted.


%package -n %{srcname}-%{sover}-devel
Summary:        Development files for %{name}
License:        LGPLv3
Group:          Development/Libraries/C and C++
Requires:       %{srcname}-%{sover} = %{version}-%{release}

%description -n %{srcname}-%{sover}-devel
Contains libraries and header files for developing applications using
%{srcname}.

%prep
%setup -q -n %{srcname}-%{srcname}-%{version}

%build
gtkdocize
autoreconf -fiv
%configure \
  --disable-static \
  --enable-gtk-doc

%make_build

%install
%make_install
find "%{buildroot}" -type f -name '*.la' -delete

%post -n %{srcname}-%{sover} -p /sbin/ldconfig

%postun -n %{srcname}-%{sover} -p /sbin/ldconfig

%files
%license COPYING.gpl
%{_bindir}/ldmtool
%{_mandir}/man1/ldmtool.1.gz

%files -n %{srcname}-%{sover}
%license COPYING.lgpl
%{_libdir}/*.so.*

%files -n %{srcname}-%{sover}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ldm-1.0.pc
%{_datadir}/gtk-doc

%changelog
* Wed Dec 01 2021 Louis Abel <tucklesepk@gmail.com> - 0.2.5-1
- Init for 0.2.5
