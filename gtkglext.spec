#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gtkglext
Version  : 1.2.0
Release  : 2
URL      : http://downloads.sourceforge.net/gtkglext/gtkglext-1.2.0.tar.gz
Source0  : http://downloads.sourceforge.net/gtkglext/gtkglext-1.2.0.tar.gz
Summary  : OpenGL Extension to GTK
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gtkglext-data = %{version}-%{release}
Requires: gtkglext-lib = %{version}-%{release}
Requires: gtkglext-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-gnome
BuildRequires : gettext-bin
BuildRequires : gfortran
BuildRequires : glu-dev
BuildRequires : gtk+-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libXt-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : mesa-dev
BuildRequires : perl
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(pangox)
BuildRequires : pkgconfig(xmu)
BuildRequires : xorg-server-dev
Patch1: build.patch
Patch2: update.patch

%description
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package data
Summary: data components for the gtkglext package.
Group: Data

%description data
data components for the gtkglext package.


%package dev
Summary: dev components for the gtkglext package.
Group: Development
Requires: gtkglext-lib = %{version}-%{release}
Requires: gtkglext-data = %{version}-%{release}
Provides: gtkglext-devel = %{version}-%{release}

%description dev
dev components for the gtkglext package.


%package doc
Summary: doc components for the gtkglext package.
Group: Documentation

%description doc
doc components for the gtkglext package.


%package lib
Summary: lib components for the gtkglext package.
Group: Libraries
Requires: gtkglext-data = %{version}-%{release}
Requires: gtkglext-license = %{version}-%{release}

%description lib
lib components for the gtkglext package.


%package license
Summary: license components for the gtkglext package.
Group: Default

%description license
license components for the gtkglext package.


%prep
%setup -q -n gtkglext-1.2.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543743912
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1543743912
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gtkglext
cp COPYING %{buildroot}/usr/share/package-licenses/gtkglext/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/gtkglext/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GdkGLExt-1.0.typelib
/usr/lib64/girepository-1.0/GtkGLExt-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gtkglext-1.0/gdk/gdkgl.h
/usr/include/gtkglext-1.0/gdk/gdkglconfig.h
/usr/include/gtkglext-1.0/gdk/gdkglcontext.h
/usr/include/gtkglext-1.0/gdk/gdkgldebug.h
/usr/include/gtkglext-1.0/gdk/gdkgldefs.h
/usr/include/gtkglext-1.0/gdk/gdkgldrawable.h
/usr/include/gtkglext-1.0/gdk/gdkglenumtypes.h
/usr/include/gtkglext-1.0/gdk/gdkglglext.h
/usr/include/gtkglext-1.0/gdk/gdkglinit.h
/usr/include/gtkglext-1.0/gdk/gdkglpixmap.h
/usr/include/gtkglext-1.0/gdk/gdkglquery.h
/usr/include/gtkglext-1.0/gdk/gdkgltokens.h
/usr/include/gtkglext-1.0/gdk/gdkgltypes.h
/usr/include/gtkglext-1.0/gdk/gdkglversion.h
/usr/include/gtkglext-1.0/gdk/gdkglwindow.h
/usr/include/gtkglext-1.0/gdk/glext/glext-extra.h
/usr/include/gtkglext-1.0/gdk/glext/glext.h
/usr/include/gtkglext-1.0/gdk/glext/glxext-extra.h
/usr/include/gtkglext-1.0/gdk/glext/glxext.h
/usr/include/gtkglext-1.0/gdk/glext/wglext-extra.h
/usr/include/gtkglext-1.0/gdk/glext/wglext.h
/usr/include/gtkglext-1.0/gdk/x11/gdkglglxext.h
/usr/include/gtkglext-1.0/gdk/x11/gdkglx.h
/usr/include/gtkglext-1.0/gtk/gtkgl.h
/usr/include/gtkglext-1.0/gtk/gtkgldebug.h
/usr/include/gtkglext-1.0/gtk/gtkgldefs.h
/usr/include/gtkglext-1.0/gtk/gtkglinit.h
/usr/include/gtkglext-1.0/gtk/gtkglversion.h
/usr/include/gtkglext-1.0/gtk/gtkglwidget.h
/usr/lib64/gtkglext-1.0/include/gdkglext-config.h
/usr/lib64/libgdkglext-x11-1.0.so
/usr/lib64/libgtkglext-x11-1.0.so
/usr/lib64/pkgconfig/gdkglext-1.0.pc
/usr/lib64/pkgconfig/gdkglext-x11-1.0.pc
/usr/lib64/pkgconfig/gtkglext-1.0.pc
/usr/lib64/pkgconfig/gtkglext-x11-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/gtkglext/GdkGLExt-API.html
/usr/share/gtk-doc/html/gtkglext/GtkGLExt-API.html
/usr/share/gtk-doc/html/gtkglext/Overview.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-building.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglconfig.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglcontext.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkgldrawable.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglfont.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglinit.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglpixmap.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglquery.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglshapes.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkgltokens.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglversion.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglwindow.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gdkglx.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gtkglinit.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gtkglversion.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-gtkglwidget.html
/usr/share/gtk-doc/html/gtkglext/gtkglext-running.html
/usr/share/gtk-doc/html/gtkglext/gtkglext.devhelp
/usr/share/gtk-doc/html/gtkglext/home.png
/usr/share/gtk-doc/html/gtkglext/index.html
/usr/share/gtk-doc/html/gtkglext/index.sgml
/usr/share/gtk-doc/html/gtkglext/left.png
/usr/share/gtk-doc/html/gtkglext/right.png
/usr/share/gtk-doc/html/gtkglext/style.css
/usr/share/gtk-doc/html/gtkglext/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgdkglext-x11-1.0.so.0
/usr/lib64/libgdkglext-x11-1.0.so.0.200.0
/usr/lib64/libgtkglext-x11-1.0.so.0
/usr/lib64/libgtkglext-x11-1.0.so.0.200.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtkglext/COPYING
/usr/share/package-licenses/gtkglext/COPYING.LIB
