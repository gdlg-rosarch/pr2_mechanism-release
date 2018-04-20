# Script generated with Bloom
pkgdesc="ROS - This package specifies the interface to a realtime controller. A controller that implements this interface can be executed by the <a href="http://www.ros.org/wiki/pr2_controller_manager">controller manager</a> in the real time control loop. The package basically contains the C++ controller base class that all controllers need to inherit from."
url='http://ros.org/wiki/pr2_controller_interface'

pkgname='ros-kinetic-pr2-controller-interface'
pkgver='1.8.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-controller-interface'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-controller-interface'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=pr2_controller_interface
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_controller_interface $srcdir/pr2_controller_interface
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

