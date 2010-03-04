%define _name OpenJPEG
%define _ver    %(echo %{version} | tr . _)
Summary:	An open-source JPEG 2000 codec
Name:		openjpeg
Version:	1.3
Release:	2
Source0:	http://openjpeg.googlecode.com/files/%{name}_v%{_ver}.tar.gz
# Source0-md5:	f9a3ccfa91ac34b589e9bf7577ce8ff9
Patch0:		%{name}-install.patch
License:	BSD
Group:		Libraries
URL:		http://www.openjpeg.org/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image compression standard from the Joint
Photographic Experts Group (JPEG).

%package devel
Summary:	Development tools for programs using the OpenJPEG library
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains the header files and libraries needed for
developing programs using the OpenJPEG library.

%prep
%setup -q -n %{_name}_v%{_ver}
%patch0 -p1

sed 's/$(CC) -s/$(CC) $(CFLAGS) $(LDFLAGS)/' -i Makefile
sed 's/-lstdc++/-lm/' -i Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_LIBDIR=%{_libdir} \
	INSTALL_INCLUDE=%{_includedir}

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libopenjpeg.so.? libopenjpeg.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjpeg-*.*.*.*.so
%attr(755,root,root) %ghost %{_libdir}/libopenjpeg.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}.h
%{_libdir}/libopenjpeg.a
%{_libdir}/libopenjpeg.so
