Summary: python module for parted
Name: pyparted
Version: 1.6.6
Release: 1
License: GPL
Group: System Environment/Libraries
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: parted
BuildRequires: parted-devel

%description
Python modules for the parted library.  It is used for manipulation
partition tables.

%prep
%setup -q

%build
export CFLAGS="-fPIC"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/python?.?/site-packages/*.so


%changelog
* Fri Mar 12 2004 Jeremy Katz <katzj@redhat.com>
- Initial build split out into separate source from the parted package.

