Name:           libxfce4util
Version:        4.14.0
Release:        1
Summary:        Basic utility library for Xfce4

License:        LGPLv2+
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/4.14/%{name}-%{version}.tar.bz2
#VCS: git:git://git.xfce.org/xfce/libxfce4util

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala

%description
This package includes basic utility non-GUI functions for Xfce4.

%package devel
Summary: Developpment tools for libxfce4util library
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk2-devel
Requires: pkgconfig

%description devel
This package includes static libraries and header files for the libxfce4util library.

%prep
%setup -q

%build

%configure --disable-static

# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/libxfce4util/.libs"

%make_build

%install
%make_install

chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*.so

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.Kiosk THANKS
%{_libdir}/lib*.so.*
%{_sbindir}/xfce4-kiosk-query
%{_libdir}/girepository-1.0/%{name}-1.0.typelib
%{_datadir}/gir-1.0/%{name}-1.0.gir
%{_datadir}/vala/vapi/%{name}-1.0.vapi

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4
%doc %{_datadir}/gtk-doc/

%changelog
* Wed Jun 10 2020 Dillon Chen <dillon.chen@turbolinux.com.cn> - 4.14.0-1
- build for openEuler

